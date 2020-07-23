#include "hello_world.h"

#include "test/catch.hpp"

TEST_CASE("test_hello")
{
    REQUIRE(hello_world::hello() == "Hello, World!");
}

TEST_CASE("test_backyard")
{
    REQUIRE(hello_world::backyard() == "OMG! There's a giant branch!");
}
