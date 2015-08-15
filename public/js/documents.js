// What to do when user clicks on item in document list
$('#documentList').find('a').click(function(event){

    event.preventDefault();

    // Correctly set the active class
    $('#documentList').find('a').removeClass('active');
    $(this).addClass('active');

    // Get the filename
    var file = $(this).data('file');
    var url = '/js/libs/pdfjs/#../../../' + file;

    // Remove existing document viewer
    $('#documentViewerContainer').empty();

    // Add new document viewer
    $('<iframe />', {
        class: 'col-sm-8',
        width: '100%',
        height: '600',
        allowfullscreen: true,
        src: file
    }).appendTo('#documentViewerContainer');

});