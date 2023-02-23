function getHTML(url) {
     fetch(url, { timeout: 5000 })
          .then(function (response) {
               if (response.ok) {
                    return response.text();
               } else {
                    throw new Error('Error loading form: ' + response.statusText);
               }
          })
          .then(function (html) {
               document.getElementById('form_container').innerHTML = html;
               console.log(html);
          })
          .catch(function (error) {
               console.error(error);
          });
}
