import plotly.graph_objects as go
from domain.services.product import ProductService

products = ProductService.get_all_product()

available_count = sum(1 for product in products if product.available)
unavailable_count = len(products) - available_count

labels = ['Available', 'Unavailable']
values = [available_count, unavailable_count]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_layout(
    title_text="Total percentage of available and unavailable products")
fig.show()
