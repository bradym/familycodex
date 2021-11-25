function renderPdf(file){
    var url = '/js/libs/pdfjs/#../../../' + file;

    // Remove existing document viewer
    $('#documentViewerContainer').empty();

    // Add new document viewer
    $('<iframe />', {
        width: '100%',
        height: '1200px',
        allowfullscreen: true,
        src: file
    }).appendTo('#documentViewerContainer');
}

$(document).ready(function() {

    // Set the first tab active. Done here because it may vary depending on what assets are
    // available for a given person.
    $('#nav-tab a:first-child').addClass('active');
    $('#nav-tabContent div:first-child').addClass('show').addClass('active');

    // Render the first document without requiring a click.
    if ($('#documentList').children().length > 0) {
        $('#documentList').children().first().addClass('active')
        renderPdf($('#documentList').children().first().data('file'));

    }

    // Render the selected PDF from the list
    $('#documentList').find('a').click(function(event){
        event.preventDefault();

        // Correctly set the active class
        $('#documentList').find('a').removeClass('active');
        $(this).addClass('active');
        renderPdf($(this).data('file'))
    });
});
