<?php

class Task
{
    protected $generator;

    public function __construct(Generator $generator)
    {
        $this->generator = $generator;
    }

    public function run()
    {
        if ($this->run) {
            $this->generator->next();
        } else {
            $this->generator->current();
        }
 
        $this->run = true;
    }

    public function finished()
    {
        return !$this->generator->valid();
    }
}

class Scheduler
{
    protected $queue;

    public function __construct()
    {
        $this->queue = new SplQueue();
    }

    public function enqueue(Task $task)
    {
        $this->queue->enqueue($task);
    }

    public function run()
    {
        while (!$this->queue->isEmpty()) {
            $task = $this->queue->dequeue();
            $task->run();

            if (!$task->finished()) {
                $this->enqueue($task);
            }
        }
    }
}

$scheduler = new Scheduler();

$task1 = new Task(call_user_func(function() {
    for ($i = 0; $i < 13; $i++) {
        print "task 1: " . $i . "\n";
        yield;
    }
}));

$task2 = new Task(call_user_func(function() {
    for ($i = 0; $i < 16; $i++) {
        print "task 2: " . $i . "\n";
        yield;
    }
}));

$scheduler->enqueue($task1);
$scheduler->enqueue($task2);

$scheduler->run();
