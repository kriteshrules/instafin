<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['News', 'No of news'],
          ['Positive', {{ pos_count }}],
          ['Negative', {{ neg_count }}],
          ['Neutral', {{ neu_count }}]
        ]);

        var data2 = google.visualization.arrayToDataTable([
          ['News', 'No of tweets'],
          ['Positive', {{ pos_countt }}],
          ['Negative', {{ neg_countt }}],
          ['Neutral', {{ neutral_count }}]
        ]);

        var options = {
          title: 'Google News Sentiment Analysis',
          is3D: true,
        };

        var options2 = {
          title: 'Twitter Sentiment Analysis',
          is3D: true,
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_google'));
        chart.draw(data, options);

        var chart = new google.visualization.PieChart(document.getElementById('piechart_twitter'));
        chart.draw(data2, options2);
      }
</script>