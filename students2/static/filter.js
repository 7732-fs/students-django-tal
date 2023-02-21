let objs = document.getElementsByClassName("update")

document.getElementById('filter').onchange = () => {
     for (const o of objs) {
          if (o.innerText.includes(filter.value)) {
               o.style.display="grid";
          }
          else {
               o.style.display="none";
          }
     }
}