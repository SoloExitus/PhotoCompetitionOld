$(document).ready(function() {
        $.ajax({
          url: "{% url 'photopost-list' %}",
          type: "GET",
          dataType: "json",
           success: (data) => {
              const gallery = $(".gallery");
              gallery.empty()

              data.forEach(postData => {

                const post = `
                    <div class="col-lg-3 col-md-4 col-6">
                  <a href="#" class="d-block mb-4 h-100">
                    <img class="img-fluid img-thumbnail" src="${postData.image}" alt="${postData.title}">
                  </a>
                  likes: ${postData.likes_count}
                  comments: ${postData.comments_count}
                </div>`

                gallery.append(post);
              });
            },
              error: (error) => {
                console.log(error);
              }
        });
        });
