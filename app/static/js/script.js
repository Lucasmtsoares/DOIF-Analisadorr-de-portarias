const grafic_nomeacao = document.getElementById('grafic-nomeacao');
const grafic_exoneracao = document.getElementById('grafic-exoneracao')
//nomeacoes
const jan_nom = document.getElementById('jan-nom').textContent
const jan_nom_data = parseInt(jan_nom)
const fev_nom = document.getElementById('fev-nom').textContent
const fev_nom_data = parseInt(fev_nom)
const marc_nom = document.getElementById('marc-nom').textContent
const marc_nom_data = parseInt(marc_nom)
const abri_nom = document.getElementById('abri-nom').textContent
const abri_nom_data = parseInt(abri_nom)
const mai_nom = document.getElementById('mai-nom').textContent
const mai_nom_data = parseInt(mai_nom)
const jun_nom = document.getElementById('jun-nom').textContent
const jun_nom_data = parseInt(jun_nom)
const jul_nom = document.getElementById('jul-nom').textContent
const jul_nom_data = parseInt(jul_nom)
const ago_nom = document.getElementById('ago-nom').textContent
const ago_nom_data = parseInt(ago_nom)
const set_nom = document.getElementById('set-nom').textContent
const set_nom_data = parseInt(set_nom)
const out_nom = document.getElementById('out-nom').textContent
const out_nom_data = parseInt(out_nom)
const nov_nom = document.getElementById('nov-nom').textContent
const nov_nom_data = parseInt(nov_nom)
const dez_nom = document.getElementById('dez-nom').textContent
const dez_nom_data = parseInt(dez_nom)

//exoneracoes

const jan_exo = document.getElementById('jan-exo').textContent
const jan_exo_data = parseInt(jan_exo)
const fev_exo = document.getElementById('fev-exo').textContent
const fev_exo_data = parseInt(fev_exo)
const marc_exo = document.getElementById('marc-exo').textContent
const marc_exo_data = parseInt(marc_exo)
const abri_exo = document.getElementById('abri-exo').textContent
const abri_exo_data = parseInt(abri_exo)
const mai_exo = document.getElementById('mai-exo').textContent
const mai_exo_data = parseInt(mai_exo)
const jun_exo = document.getElementById('jun-exo').textContent
const jun_exo_data = parseInt(jun_exo)
const jul_exo = document.getElementById('jul-exo').textContent
const jul_exo_data = parseInt(jul_exo)
const ago_exo = document.getElementById('ago-exo').textContent
const ago_exo_data = parseInt(ago_exo)
const set_exo = document.getElementById('set-exo').textContent
const set_exo_data = parseInt(set_exo)
const out_exo = document.getElementById('out-exo').textContent
const out_exo_data = parseInt(out_exo)
const nov_exo = document.getElementById('nov-exo').textContent
const nov_exo_data = parseInt(nov_exo)
const dez_exo = document.getElementById('dez-exo').textContent
const dez_exo_data = parseInt(dez_exo)

new Chart(grafic_nomeacao, {
  type: 'line',
  data: {
    labels: ['Jan', 'Fev', 'Mar', 'Abri', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    datasets: [{
      label: 'Nomeações',
      data: [jan_nom_data, fev_nom_data, marc_nom_data, abri_nom_data, mai_nom_data, jun_nom_data, jul_nom_data, ago_nom_data, set_nom_data, out_nom_data, nov_nom_data, dez_nom_data],
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
new Chart(grafic_exoneracao, {
  type: 'line',
  data: {
    labels: ['Jan', 'Fev', 'Mar', 'Abri', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    datasets: [{
      label: 'Exonerações',
      data: [jan_exo_data, fev_exo_data, marc_exo_data, abri_exo_data, mai_exo_data, jun_exo_data, jul_exo_data, ago_exo_data, set_exo_data, out_exo_data, nov_exo_data, dez_exo_data],
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