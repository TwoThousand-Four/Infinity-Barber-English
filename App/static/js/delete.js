function delete_service(id){
    Swal.fire({
        title: "Are you sure to delete this service?",
        text: "This change cannot be reversed!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete!"
      }).then(function(result){
        if(result.isConfirmed){
            window.location.href="/eliminar/"+id+"/"
        }
    });
}