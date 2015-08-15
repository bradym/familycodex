<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Person extends Model
{
    protected $table = 'people';

    public function family() {
        return $this->belongsToMany('\App\Family');
    }





    public function relationship() {
        return $this->hasMany('\App\Relationship');
    }

    public function asset() {
        return $this->hasMany('\App\Asset');
    }


    public function getFullName() {

        $fullName = $this->first_name;

        $fullName .= !empty($this->middle_name) ? ' ' . $this->middle_name : null;
        $fullName .= !empty($this->maiden_name) ? ' ' . $this->maiden_name : null;
        $fullName .= !empty($this->last_name)   ? ' ' . $this->last_name   : null;

        return $fullName;

    }



}
