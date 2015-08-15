<?php

use Illuminate\Database\Seeder;

class RelationshipTypesSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $now = date('Y-m-d H:i:s');

        DB::table('relationship_types')->insert([
            ['name' => 'Spouse', 'created_at' => $now],
            ['name' => 'Parent', 'created_at' => $now],
            ['name' => 'Child',  'created_at' => $now],
        ]);
    }
}
