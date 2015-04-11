import plotly.plotly as py
from plotly.graph_objs import *


class TrendGraph:
    def __init__(self, input_data):
        self.green = Bar(
                x=input_data['dates'],
                y=input_data['green'],
                marker = Marker(
                    color = 'green'
                    ),
                name = "Green"
        )

        self.libertarian = Bar(
                x=input_data['dates'],
                y=input_data['libertarian'],
                marker = Marker(
                    color = 'yellow'
                    ),
                name = "Libertarian"
        )

        self.liberal = Bar(
                x=input_data['dates'],
                y=input_data['liberal'],
                marker = Marker(
                    color = 'blue'
                    ),
                name = "Liberal"
        )

        self.conservative = Bar(
                x=input_data['dates'],
                y=input_data['conservative'],
                marker = Marker(
                    color = 'red'
                    ),
                name = "Conservative"
        )

        self.data = Data([self.green, self.libertarian, self.liberal, self.conservative])
        self.layout = Layout(
            barmode = 'stack'
        )

        self.fig = Figure(data=self.data, layout=self.layout)

    def getGraph(self):
        self.plot_url = py.plot(self.fig, filename='stacked-bar')


