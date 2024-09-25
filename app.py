from flask import Flask, request, jsonify, render_template, Response
import subprocess
import threading
import logging
import queue
import time

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# 创建一个队列来存储日志消息
log_queue = queue.Queue()

def log_reader(process, queue):
    for line in iter(process.stdout.readline, ''):
        queue.put(line)
    process.stdout.close()

@app.route('/')
def index():
    return render_template('index.html')

def run_script_async(data):
    command = [
        'python', 'main.py',
        data['account'], data['password'], data['schoolName'],
        str(int(data['autoVerify'])), str(data['projectIndex']),
        str(data['autoExam']), str(data['examThreshold'])
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
        
        # 启动一个线程来读取进程的输出
        thread = threading.Thread(target=log_reader, args=(process, log_queue))
        thread.start()

        # 等待进程完成
        process.wait()

        if process.returncode != 0:
            log_queue.put(f"Process exited with return code {process.returncode}")
    except Exception as e:
        log_queue.put(f"An error occurred: {str(e)}")

@app.route('/run', methods=['POST'])
def run_script():
    data = request.json
    threading.Thread(target=run_script_async, args=(data,)).start()
    return jsonify({'message': 'Script execution started'}), 202

@app.route('/stream')
def stream():
    def generate():
        while True:
            try:
                # 非阻塞方式从队列中获取消息
                message = log_queue.get_nowait()
                yield f"data: {message}\n\n"
            except queue.Empty:
                time.sleep(0.1)  # 短暂休眠以减少 CPU 使用
    return Response(generate(), mimetype='text/event-stream')

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled exception: {str(e)}", exc_info=True)
    return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)