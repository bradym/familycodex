@extends('layouts.master')
@section('title', $title)
@section('pageHeading', $title)

@section('content')

    @foreach ($family->person as $person)

        <div class="col-md-4 text-center">
            <div class="thumbnail">
                <img class="img-responsive" src="http://placehold.it/750x450" alt="">
                <div class="caption">
                    <h3><a href="{{$person->slug}}.html">{{$person->getFullName()}}</a></h3>
                </div>
            </div>
        </div>

    @endforeach

@endsection
