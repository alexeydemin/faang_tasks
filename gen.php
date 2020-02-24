<?php

$generator = call_user_func(function() {
    $input = (yield "foo");
    print "inside: " . $input . "\n";
});

print $generator->current() . "\n";

$generator->send("bar");
