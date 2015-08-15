<?php

namespace App\Http\Controllers;

use App\Family;
use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;

/**
 * Class HomeController
 * @package App\Http\Controllers
 *
 * Handles the home page of www.familycodex.net
 */

class HomeController extends Controller
{

    /**
     * List all families in the system and let user select one to view.
     *
     * @return \Illuminate\View\View
     */
    function index() {

        $familes = Family::all();

        return view('welcome', ['families' => $familes]);
    }
}
