@extends('layouts.master')
@section('title', 'Welcome to FamilyCodex.net')

@section('content')

    <ul>
        @foreach ($families as $family)
            <li><a href='//{{$family->slug}}.familycodex.dev'>{{$family->name}}</a></li>
        @endforeach
    </ul>

@endsection
