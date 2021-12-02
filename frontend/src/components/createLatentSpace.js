import Highcharts from 'highcharts'
import More from 'highcharts/highcharts-more'
import draggablePoints from 'highcharts/modules/draggable-points'

More(Highcharts)
draggablePoints(Highcharts)
var companyTableData = {
  company: ''
}

var termTableData = {
  term: ''
}

const chartOptions = {
  tooltip: {
    valueDecimals: 9
  },
  xAxis: {
    // min: -1,
    // max: 1,
    gridLineWidth: 1,
    tickPixelInterval: 25
  },
  yAxis: {
    // min: -1,
    // max: 1,
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
      name: 'Company',
      data: [],
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
            const point = this
            const index = point.index
            companyTableData.company = chartOptions.series[0].dataLabal[index]
          },
          drop: function (e) {
            const point = this
            const index = point.index
            if (e.newPoint.x !== undefined) {
              chartOptions.series[0].data[index] = [e.newPoint.x, e.newPoint.y]
            }
          }
        }
      }
    },
    {
      name: 'Term',
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
            termTableData.term =
              chartOptions.series[1].dataLabal[index]
          },
          drop: function (e) {
            const point = this
            const index = point.index
            if (e.newPoint.x !== undefined) {
              chartOptions.series[1].data[index] = [e.newPoint.x, e.newPoint.y]
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

export { companyTableData, termTableData, chartOptions }
