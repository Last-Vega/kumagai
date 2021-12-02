import Highcharts from 'highcharts'
import More from 'highcharts/highcharts-more'
import draggablePoints from 'highcharts/modules/draggable-points'

More(Highcharts)
draggablePoints(Highcharts)
var tableData = {
  title: '',
  author: '',
  conference: '',
  year: ''
}

var miscList = []

var reMovedObj = {}

const chartOptions = {
  tooltip: {
    valueDecimals: 9
  },
  xAxis: {
    min: -1,
    max: 1,
    gridLineWidth: 1,
    tickPixelInterval: 25
  },
  yAxis: {
    min: -1,
    max: 1,
    tickPixelInterval: 50
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    verticalAlign: 'top',
    floating: true,
    backgroundColor: Highcharts.defaultOptions.chart.backgroundColor,
    borderWidth: 1
  },
  title: {
    text: '潜在空間'
  },
  series: [
    {
      name: '動かす文献',
      data: [[0, 0]],
      dataLabal: [],
      type: 'scatter',
      animation: false,
      dragDrop: {
        draggableX: true,
        draggableY: true,
        liveRedraw: true
      },
      point: {
        events: {
          mouseOver () {
            tableData.title = ''
            tableData.author = ''
            tableData.conference = ''
            tableData.year = ''
          },
          drop: function (e) {
            const point = this
            const index = point.index
            if (e.newPoint.x !== undefined) {
              chartOptions.series[0].data[index] = [e.newPoint.x, e.newPoint.y]
              miscList[index] = [e.newPoint.x, e.newPoint.y]
              console.log(miscList)
            }
          }
        }
      }
    },
    {
      name: '動かした文献',
      data: [],
      dataLabal: [],
      type: 'scatter',
      color: 'red',
      animation: false,
      dragDrop: {
        draggableX: true,
        draggableY: true,
        liveRedraw: true
      },
      point: {
        events: {
          mouseOver () {
            const point = this
            const index = point.index
            tableData.title =
              chartOptions.series[1].dataLabal[index][0].title
            tableData.author =
              chartOptions.series[1].dataLabal[index][0].author
            tableData.conference =
              chartOptions.series[1].dataLabal[index][0].conference
            tableData.year = chartOptions.series[1].dataLabal[index][0].year
          },
          drop: function (e) {
            const point = this
            const index = point.index
            if (e.newPoint.x !== undefined) {
              console.log(e.newPoint.x)
              chartOptions.series[1].data[index] = [e.newPoint.x, e.newPoint.y]
              reMovedObj[index] = [e.newPoint.x, e.newPoint.y]
            }
          }
        }
      }
    }
  ],
  plotOptions: {
    series: {
      states: {
        hover: {
          enabled: false
        }
      }
    }
  }
}

export { tableData, chartOptions, miscList, reMovedObj }
