<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Symfony\Component\Process\Process;


class LocalSetup extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'local:setup';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Automate setup of local environment';

    /**
     * Create a new command instance.
     */
    public function __construct()
    {
        parent::__construct();
    }

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
        $basePath = $this->getLaravel()->basePath() . '/';

        // Get user input
        $input = [
            'host'     => 'localhost',
            'dbname'   => 'familycodex',
            'username' => 'homestead',
            'password' => 'secret',
        ];

        // Create .env
        $envTemplate = file_get_contents($basePath . '.env.example');

        file_put_contents($basePath . '.env', vsprintf($envTemplate, $input));

        // Install dependencies
        $process = new Process('composer install');
        $process->run();

        $process = new Process('bower install');
        $process->run();

        // Generate app key
        $this->call('key:generate');

        // Run db migrations
        $this->call('migrate:install');
        $this->call('migrate');

        // Run db seeds
        $this->call('db:seed');

        // Generate ide helpers
        $this->call('ide-helper:generate');
        $this->call('ide-helper:models', ['--nowrite' => 'Yes']);
        $this->call('ide-helper:meta');

        // Publish vendor assets
        $this->call('vendor:publish');

        // Optimize for performance
        $this->call('optimize');
    }
}
