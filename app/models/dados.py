
res = {
    'January': {
        'Nomeacoes': 1,
        'Exoneracoes': 7,
        'Outros': 10
    },
    'February': {
        'Nomeacoes': 78,
        'Exoneracoes': 3,
        'Outros': 10 
    },
    'March': {
        'Nomeacoes': 0,
        'Exoneracoes': 1,
        'Outros': 8
    },
    'April': {
        'Nomeacoes': 1,
        'Exoneracoes': 6,
        'Outros': 11
    },
    'May': {
        'Nomeacoes': 6,
        'Exoneracoes': 2,
        'Outros': 9
    },
    'June': {
        'Nomeacoes': 44,
        'Exoneracoes': 29,
        'Outros': 16
    },
    'July': {
        'Nomeacoes': 18,
        'Exoneracoes': 18,
        'Outros': 12
    },
    'August': {
        'Nomeacoes': 2,
        'Exoneracoes': 1,
        'Outros': 18
    },
    'September': {
        'Nomeacoes': 12,
        'Exoneracoes': 3,
        'Outros': 20
    },
    'October': {
        'Nomeacoes': 1,
        'Exoneracoes': 2,
        'Outros': 19
    },
    'November': {
        'Nomeacoes': 24,
        'Exoneracoes': 1,
        'Outros': 14
    },
    'December': {
        'Nomeacoes': 35,
        'Exoneracoes': 0,
        'Outros': 30
    },
    #total: 397
}

def salve():
    print("Salve-se quem puder")

"""
2022

{
'January':   {'Nomeacoes': 4, 'Exoneracoes': 6, 'Outros': 10}, '
February':   {'Nomeacoes': 2, 'Exoneracoes': 6, 'Outros': 9}, 
'March':     {'Nomeacoes': 2, 'Exoneracoes': 1, 'Outros': 11}, 
'April':     {'Nomeacoes': 19, 'Exoneracoes': 3, 'Outros': 10}, 
'May':       {'Nomeacoes': 10, 'Exoneracoes': 1, 'Outros': 24}, 
'June':      {'Nomeacoes': 8, 'Exoneracoes': 3, 'Outros': 31}, 
'July':      {'Nomeacoes': 8, 'Exoneracoes': 3, 'Outros': 14}, 
'August':    {'Nomeacoes': 16, 'Exoneracoes': 1, 'Outros': 16}, 
'September': {'Nomeacoes': 15, 'Exoneracoes': 2, 'Outros': 19}, 
'October':   {'Nomeacoes': 3, 'Exoneracoes': 2, 'Outros': 14}, 
'November':  {'Nomeacoes': 4, 'Exoneracoes': 1, 'Outros': 2}, 
'December':  {'Nomeacoes': 4, 'Exoneracoes': 3, 'Outros': 13}}
"""

"""
2023

datas = {
'January':   {'Nomeacoes': 1, 'Exoneracoes': 7, 'Outros': 10}, 
'February':  {'Nomeacoes': 3, 'Exoneracoes': 3, 'Outros': 10}, 
'March':     {'Nomeacoes': 3, 'Exoneracoes': 1, 'Outros': 8}, 
'April':     {'Nomeacoes': 1, 'Exoneracoes': 6, 'Outros': 11}, 
'May':       {'Nomeacoes': 6, 'Exoneracoes': 2, 'Outros': 9}, 
'June':      {'Nomeacoes': 44, 'Exoneracoes': 29, 'Outros': 16}, 
'July':      {'Nomeacoes': 18, 'Exoneracoes': 18, 'Outros': 12}, 
'August':    {'Nomeacoes': 2, 'Exoneracoes': 1, 'Outros': 18}, 
'September': {'Nomeacoes': 12, 'Exoneracoes': 3, 'Outros': 20}, 
'October':   {'Nomeacoes': 1, 'Exoneracoes': 2, 'Outros': 19},
'November':  {'Nomeacoes': 24, 'Exoneracoes': 1, 'Outros': 14}, 
'December':  {'Nomeacoes': 35, 'Exoneracoes': 1, 'Outros': 30}}

"""

"""
IFPE 2022

{'January': {'Nomeacoes': 17, 'Exoneracoes': 2, 'Outros': 41}, 
'February': {'Nomeacoes': 18, 'Exoneracoes': 1, 'Outros': 45}, 
'March': {'Nomeacoes': 11, 'Exoneracoes': 2, 'Outros': 46}, 
'April': {'Nomeacoes': 9, 'Exoneracoes': 3, 'Outros': 44}, 
'May': {'Nomeacoes': 15, 'Exoneracoes': 5, 'Outros': 79}, 
'June': {'Nomeacoes': 9, 'Exoneracoes': 2, 'Outros': 65}, 
'July': {'Nomeacoes': 14, 'Exoneracoes': 2, 'Outros': 71}, 
'August': {'Nomeacoes': 11, 'Exoneracoes': 1, 'Outros': 63}, 
'September': {'Nomeacoes': 11, 'Exoneracoes': 7, 'Outros': 53}, 
'October': {'Nomeacoes': 5, 'Exoneracoes': 1, 'Outros': 55}, 
'November': {'Nomeacoes': 9, 'Exoneracoes': 1, 'Outros': 47}, 
'December': {'Nomeacoes': 10, 'Exoneracoes': 1, 'Outros': 16}}

"""

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>analisar_portarias</title>
    <style>
        body{
          margin: 0;
          padding: 0;
        }
        .content{
            width: 50%;
            height: 20%;
            background-color: bisque;
        }
        .v{
          background-color: blueviolet;
        }
    </style>
</head>
<body>
  <header class="v">
    teste
  </header>
    <h1>Gráficos</h1>
    

    <div class="content">
        <div>
            <canvas id="myChart"></canvas>
          </div>
    </div>
    
    <script src="https://cdn.jsdejlivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 190, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
</script>
</body>
</html>
"""