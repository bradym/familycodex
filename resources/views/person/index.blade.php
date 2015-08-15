@extends('layouts.master')
@section('title', $title)
@section('pageHeading', $title)

@section('css')
    <link rel="stylesheet" href="/vendor/blueimp-gallery/css/blueimp-gallery.min.css">
    <link rel="stylesheet" href="/vendor/blueimp-gallery/css/blueimp-gallery-indicator.css">
@endsection

@section('js')
    <script src="/vendor/blueimp-gallery/js/jquery.blueimp-gallery.min.js"></script>
    <script src="/js/photos.js"></script>
    <script src="/js/documents.js"></script>
@endsection

@section('content')
    <div class="row">
        <div class="col-md-6">
            <img class="img-responsive" src="http://placehold.it/750x450" alt="">
        </div>
        <div class="col-md-6">
            <h2>{{$person->getFullName()}}</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed voluptate nihil eum consectetur similique? Consectetur, quod, incidunt, harum nisi dolores delectus reprehenderit voluptatem perferendis dicta dolorem non blanditiis ex fugiat.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe, magni, aperiam vitae illum voluptatum aut sequi impedit non velit ab ea pariatur sint quidem corporis eveniet. Odit, temporibus reprehenderit dolorum!</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Et, consequuntur, modi mollitia corporis ipsa voluptate corrupti eum ratione ex ea praesentium quibusdam? Aut, in eum facere corrupti necessitatibus perspiciatis quis?</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Et, consequuntur, modi mollitia corporis ipsa voluptate corrupti eum ratione ex ea praesentium quibusdam? Aut, in eum facere corrupti necessitatibus perspiciatis quis?</p>
        </div>
    </div>

    <div class="row">
        <div role="tabpanel">

            <!-- Nav tabs -->
            <div class="panel panel-default">
                <div class="panel-body">
                    <ul class="nav nav-pills nav-justified">
                        <li role="presentation" class="active"><a href="#documents" data-toggle="tab">Documents</a></li>
                        <li role="presentation"><a href="#photos" data-toggle="tab">Photos</a></li>
                        <li role="presentation"><a href="#audio" data-toggle="tab">Audio Recordings</a></li>
                        <li role="presentation"><a href="#video" data-toggle="tab">Videos</a></li>
                    </ul>
                </div>
            </div>

            <!-- Tab panes -->
            <div class="tab-content">

                <!-- Documents -->
                <div role="tabpanel" class="tab-pane active" id="documents">

                    <div id="documentList" class="list-group col-md-4">
                        <a href="#" class="list-group-item" data-file="http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf">Document 1</a>
                        <a href="#" class="list-group-item" data-file="http://www.jorns.ch/upload/occasionen/1/190/reference1.pdf">Document 2</a>
                    </div>

                    <div id="documentViewerContainer" class="col-md-8"></div>

                </div>

                <!-- Photos -->
                <div role="tabpanel" class="tab-pane" id="photos">

                    <div id="links" class="links"></div>

                    <div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">
                        <div class="slides"></div>
                        <h3 class="title"></h3>
                        <a class="prev">‹</a>
                        <a class="next">›</a>
                        <a class="close">×</a>
                        <a class="play-pause"></a>
                        <ol class="indicator"></ol>
                    </div>

                </div>

                <!-- Audio Recordings -->
                <div role="tabpanel" class="tab-pane" id="audio">
                    <h3>Hunting Stories</h3>
                    <audio controls>
                        <source src="https://s3-us-west-1.amazonaws.com/gramps-granny/deer-hunt/deer-hunt_1.mp3"
                                type="audio/mpeg"/>
                        <a href="https://s3-us-west-1.amazonaws.com/gramps-granny/deer-hunt/deer-hunt_1.mp3">Hunting
                            Stories</a>
                        An html5-capable browser is required to play this audio.
                    </audio>
                </div>

                <!-- Video Recordings -->
                <div role="tabpanel" class="tab-pane" id="video">

                </div>
            </div>
        </div>
    </div>





@endsection
