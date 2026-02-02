report:
	jupyter nbconvert notebooks/business_insights/01_sales_insights.ipynb --to html
	mv notebooks/business_insights/*.html reports/business_insights/
