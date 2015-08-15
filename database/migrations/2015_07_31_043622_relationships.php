<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class Relationships extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('relationships', function (Blueprint $table) {
            $table->increments('id');
            $table->integer('family_id')->unsigned();;
            $table->integer('person_1_id')->unsigned();
            $table->integer('person_2_id')->unsigned();;
            $table->integer('relationship_type_code')->unsigned();;
            $table->integer('person_1_role_id')->unsigned();;
            $table->integer('person_2_role_id')->unsigned();;
            $table->date('date_relationship_started');
            $table->date('date_relationship_ended');
            $table->timestamps();
            $table->softDeletes();
            $table->foreign('person_1_id')->references('id')->on('people');
            $table->foreign('person_2_id')->references('id')->on('people');
            $table->foreign('relationship_type_code')->references('id')->on('relationship_types');
            $table->foreign('person_1_role_id')->references('id')->on('relationship_roles');
            $table->foreign('person_2_role_id')->references('id')->on('relationship_roles');

        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('relationships');
    }
}
