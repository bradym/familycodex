<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class PersonFamily extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('person_family', function (Blueprint $table) {
            $table->integer('person_id')->unsigned();
            $table->integer('family_id')->unsigned();
            $table->timestamps();
            $table->softDeletes();
            $table->unique(['person_id', 'family_id']);
            $table->foreign('person_id')->references('id')->on('people');
            $table->foreign('family_id')->references('id')->on('families');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('person_family');
    }
}
