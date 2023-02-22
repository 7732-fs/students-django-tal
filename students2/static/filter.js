
document.getElementById('filter').onkeyup = () => {
     let objs = document.getElementsByClassName("update")
     for (const o of objs) {
          if (o.innerText.includes(filter.value)) {
               o.style.display="grid";
          }
          else {
               o.style.display="none";
          }
     }
}