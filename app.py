from flask import Flask, request, render_template
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stats = None
    plot_url = None
    if request.method == 'POST':
        try:
            p_size = int(request.form.get('pop_size', 10000))
            s_size = int(request.form.get('sample_size', 100))
            s_size = min(s_size, p_size)

            # 1. Simulate Election: 51% vote for Candidate A (The "True" Result)
            true_p = 0.55
            population = np.random.choice([0, 1], size=p_size, p=[1-true_p, true_p])
            sample = np.random.choice(population, size=s_size, replace=False)

            pop_support = np.mean(population) * 100
            sample_support = np.mean(sample) * 100
            
            # 2. Calculate Margin of Error (95% Confidence)
            # Formula: 1.96 * sqrt(p*(1-p)/n)
            z = 1.96
            moe = z * np.sqrt((sample_support/100 * (1 - sample_support/100)) / s_size) * 100

            stats = {
                "pop_support": round(pop_support, 1),
                "sample_support": round(sample_support, 1),
                "moe": round(moe, 1),
                "error": round(abs(pop_support - sample_support), 1)
            }

            # 3. Create the Comparison Bar Chart
            plt.clf()
            fig, ax = plt.subplots(figsize=(8, 6))
            
            categories = ['Actual Population', 'Exit Poll (Sample)']
            values = [pop_support, sample_support]
            errors = [0, moe] # Population has no sampling error; sample does
            
            bars = ax.bar(categories, values, yerr=errors, capsize=10, 
                          color=['#3498db', '#2ecc71'], alpha=0.8)
            
            # Add a "50% Win Line" to show if the poll predicts the wrong winner
            ax.axhline(50, color='red', linestyle='--', label='Win Threshold (50%)')
            
            ax.set_ylabel('Support for Candidate A (%)')
            ax.set_ylim(0, 100)
            ax.set_title(f'Election Reality vs. Poll (n={s_size})')
            ax.legend()

            # Save plot to base64
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
            plt.close(fig)
		
		except Exception as e:
			print(f"Error: {e}")

	return render_template('index.html', stats=stats, plot_url=plot_url)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
