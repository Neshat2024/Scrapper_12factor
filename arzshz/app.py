from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/<path:filename>')
def get_pictures(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/it')
def home_it():
    return render_template('base-it.html')

@app.route('/admin-processes')
def admin_processes():
    return render_template('admin-processes.html')

@app.route('/admin-processes-it')
def admin_processes_it():
    return render_template('admin-processes-it.html')

@app.route('/backing-services')
def backing_services():
    return render_template('backing-services.html')

@app.route('/backing-services-it')
def backing_services_it():
    return render_template('backing-services-it.html')

@app.route('/build-release-run')
def build_release_run():
    return render_template('build-release-run.html')

@app.route('/build-release-run-it')
def build_release_run_it():
    return render_template('build-release-run-it.html')

@app.route('/codebase')
def codebase():
    return render_template('codebase.html')

@app.route('/codebase-it')
def codebase_it():
    return render_template('codebase-it.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/config-it')
def config_it():
    return render_template('config-it.html')

@app.route('/concurrency')
def concurrency():
    return render_template('concurrency.html')

@app.route('/concurrency-it')
def concurrency_it():
    return render_template('concurrency-it.html')

@app.route('/dependencies')
def dependencies():
    return render_template('dependencies.html')

@app.route('/dependencies-it')
def dependencies_it():
    return render_template('dependencies-it.html')

@app.route('/dev-prod-parity')
def dev_prod_parity():
    return render_template('dev-prod-parity.html')

@app.route('/dev-prod-parity-it')
def dev_prod_parity_it():
    return render_template('dev-prod-parity-it.html')

@app.route('/disposability')
def disposability():
    return render_template('disposability.html')

@app.route('/disposability-it')
def disposability_it():
    return render_template('disposability-it.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/logs-it')
def logs_it():
    return render_template('logs-it.html')

@app.route('/port-binding')
def port_binding():
    return render_template('port-binding.html')

@app.route('/port-binding-it')
def port_binding_it():
    return render_template('port-binding-it.html')

@app.route('/processes')
def processes():
    return render_template('processes.html')

@app.route('/processes-it')
def processes_it():
    return render_template('processes-it.html')

if __name__ == '__main__':
    app.run(debug=True)