
document.getElementById('filter').onkeyup = () => {
     let objs = document.getElementsByClassName("item")
     for (const o of objs) {
          if (o.innerText.includes(filter.value)) {
               o.style.display="grid";
          }
          else {
               o.style.display="none";
          }
     }
}