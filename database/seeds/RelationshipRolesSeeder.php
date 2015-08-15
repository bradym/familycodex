<?php

use Illuminate\Database\Seeder;

class RelationshipRolesSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $now = date('Y-m-d H:i:s');

        DB::table('relationship_roles')->insert([
            ['name' => 'Father',   'created_at' => $now],
            ['name' => 'Mother',   'created_at' => $now],
            ['name' => 'Son',      'created_at' => $now],
            ['name' => 'Daughter', 'created_at' => $now],
            ['name' => 'Husband',  'created_at' => $now],
            ['name' => 'Wife',     'created_at' => $now],
        ]);

    }
}
