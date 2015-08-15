<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class PersonAssets extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('person_assets', function (Blueprint $table) {
            $table->integer('person_id')->unsigned();
            $table->integer('asset_id')->unsigned();
            $table->timestamps();
            $table->softDeletes();
            $table->unique(['person_id','asset_id']);
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('person_assets');
    }
}
