from flask import Flask, request, render_template_string
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	stats = None
	plot_url = None
	if request.method == 'POST':
		try:
			p_size = int(request.form.get('pop_size'))
			s_size = int(request.form.get('sample_size'))
			s_size = min(s_size, p_size)

			population = np.random.normal(loc=50, scale=10, size=p_size)
			sample = np.random.choice(population, size=s_size, replace=False)

			stats = {
				"pop_mean": round(np.mean(population), 2),
				"pop_var": round(np.var(population), 2),
				"sample_mean": round(np.mean(sample), 2),
				"sample_var": round(np.var(sample), 2)
			}

			plt.clf()
			plt.close('all')
			plt.figure(figsize=(8, 5))
			plt.hist(population, bins=30, alpha=0.4, label='Population', color='blue', density=True)
			plt.hist(sample, bins=30, alpha=0.6, label='Sample', color='green', density=True)
			plt.xlabel('Value of Data Points')
			plt.ylabel('Probability Density')
			plt.legend()
			plt.grid(True, linestyle='--', alpha=0.6)
			plt.title(f'Distribution: Pop({p_size}) vs Sample({s_size})')

			buf = io.BytesIO()
			plt.savefig(buf, format='png', bbox_inches='tight')
			buf.seek(0)
			plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
			plt.close()

		except Exception as e:
			print(f"Error: {e}")

	return render_template_string(index.html, stats=stats, plot_url=plot_url)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)