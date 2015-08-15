<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Family extends Model
{
    protected $table = 'families';


    public function person() {
        return $this->belongsToMany('\App\Person');
    }

}
