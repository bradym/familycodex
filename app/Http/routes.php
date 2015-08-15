<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

/**
 * Routes for www subdomain
 */
Route::group(['domain' => 'www.familycodex.dev'], function () {
    Route::get('/', [ 'uses' => 'HomeController@index']);
});


/**
 * Routes for family subdomains
 */
Route::group(['domain' => '{slug}.familycodex.dev'], function () {
    Route::get('/', [ 'uses' => 'FamilyController@index']);

    Route::get('{slug}.html', ['uses' => 'PersonController@index']);

});





