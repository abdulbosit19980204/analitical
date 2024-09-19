// basic message 
$(document).on('click', '#swt1', function(e) {
	Swal.fire('Any fool can use a computer')
});

// title with a text under
$(document).on('click', '#swt2', function(e) {
	Swal.fire(
	  'The Internet?',
	  'That thing is still around?',
	  'question'
	)
});


// basic message 
$(document).on('click', '#swt3', function(e) {
	Swal.fire({
	  icon: 'error',
	  title: 'Oops...',
	  text: 'Something went wrong!',
	  footer: '<a href="">Why do I have this issue?</a>'
	})
});



// basic message 
$(document).on('click', '#swt4', function(e) {
	Swal.fire({
  imageUrl: 'https://placeholder.pics/svg/300x1500',
  imageHeight: 1500,
  imageAlt: 'A tall image'
})
});


// basic message 
$(document).on('click', '#swt5', function(e) {
	Swal.fire({
  title: '<strong>HTML <u>example</u></strong>',
  icon: 'info',
  html:
    'You can use <b>bold text</b>, ' +
    '<a href="//sweetalert2.github.io">links</a> ' +
    'and other HTML tags',
  showCloseButton: true,
  showCancelButton: true,
  focusConfirm: false,
  confirmButtonText:
    '<i class="fa fa-thumbs-up"></i> Great!',
  confirmButtonAriaLabel: 'Thumbs up, great!',
  cancelButtonText:
    '<i class="fa fa-thumbs-down"></i>',
  cancelButtonAriaLabel: 'Thumbs down'
})
});




// basic message 
$(document).on('click', '#swt6', function(e) {
	Swal.fire({
  title: 'Do you want to save the changes?',
  showDenyButton: true,
  showCancelButton: true,
  confirmButtonText: 'Save',
  denyButtonText: `Don't save`,
}).then((result) => {
  /* Read more about isConfirmed, isDenied below */
  if (result.isConfirmed) {
    Swal.fire('Saved!', '', 'success')
  } else if (result.isDenied) {
    Swal.fire('Changes are not saved', '', 'info')
  }
})
});



// basic message 
$(document).on('click', '#swt7', function(e) {
	Swal.fire({
  position: 'top-end',
  icon: 'success',
  title: 'Your work has been saved',
  showConfirmButton: false,
  timer: 1500
})
});



// basic message 
$(document).on('click', '#swt8', function(e) {
	Swal.fire({
  title: 'Custom animation with Animate.css',
  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})
});



// basic message 
$(document).on('click', '#swt9', function(e) {
	Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      'Deleted!',
      'Your file has been deleted.',
      'success'
    )
  }
})
});



// basic message 
$(document).on('click', '#swt10', function(e) {
	const swalWithBootstrapButtons = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

swalWithBootstrapButtons.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Yes, delete it!',
  cancelButtonText: 'No, cancel!',
  reverseButtons: true
}).then((result) => {
  if (result.isConfirmed) {
    swalWithBootstrapButtons.fire(
      'Deleted!',
      'Your file has been deleted.',
      'success'
    )
  } else if (
    /* Read more about handling dismissals below */
    result.dismiss === Swal.DismissReason.cancel
  ) {
    swalWithBootstrapButtons.fire(
      'Cancelled',
      'Your imaginary file is safe :)',
      'error'
    )
  }
})
});



// basic message 
$(document).on('click', '#swt11', function(e) {
	Swal.fire({
  title: 'Sweet!',
  text: 'Modal with a custom image.',
  imageUrl: 'https://unsplash.it/400/200',
  imageWidth: 400,
  imageHeight: 200,
  imageAlt: 'Custom image',
})
});



// basic message 
$(document).on('click', '#swt12', function(e) {
	Swal.fire({
  title: 'Custom width, padding, color, background.',
  width: 600,
  padding: '3em',
  color: '#716add',
  background: '#fff url(/images/trees.png)',
  backdrop: `
    rgba(0,0,123,0.4)
    url("/images/nyan-cat.gif")
    left top
    no-repeat
  `
})
});


// basic message 
$(document).on('click', '#swt13', function(e) {
	let timerInterval
Swal.fire({
  title: 'Auto close alert!',
  html: 'I will close in <b></b> milliseconds.',
  timer: 2000,
  timerProgressBar: true,
  didOpen: () => {
    Swal.showLoading()
    const b = Swal.getHtmlContainer().querySelector('b')
    timerInterval = setInterval(() => {
      b.textContent = Swal.getTimerLeft()
    }, 100)
  },
  willClose: () => {
    clearInterval(timerInterval)
  }
}).then((result) => {
  /* Read more about handling dismissals below */
  if (result.dismiss === Swal.DismissReason.timer) {
    console.log('I was closed by the timer')
  }
})
});


// basic message 
$(document).on('click', '#swt14', function(e) {
	Swal.fire({
  title: 'هل تريد الاستمرار؟',
  icon: 'question',
  iconHtml: '؟',
  confirmButtonText: 'نعم',
  cancelButtonText: 'لا',
  showCancelButton: true,
  showCloseButton: true
})
});



// basic message 
$(document).on('click', '#swt15', function(e) {
	Swal.fire({
  title: 'Submit your Github username',
  input: 'text',
  inputAttributes: {
    autocapitalize: 'off'
  },
  showCancelButton: true,
  confirmButtonText: 'Look up',
  showLoaderOnConfirm: true,
  preConfirm: (login) => {
    return fetch(`//api.github.com/users/${login}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response.json()
      })
      .catch(error => {
        Swal.showValidationMessage(
          `Request failed: ${error}`
        )
      })
  },
  allowOutsideClick: () => !Swal.isLoading()
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire({
      title: `${result.value.login}'s avatar`,
      imageUrl: result.value.avatar_url
    })
  }
})
});
