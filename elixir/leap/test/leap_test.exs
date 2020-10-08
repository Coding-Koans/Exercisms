defmodule LeapTest do
  use ExUnit.Case

  test "vanilla leap year" do
    assert Year.leap_year?(1996)
  end

  test "any old year" do
    refute Year.leap_year?(1997), "1997 is not a leap year."
  end

  test "another any old year" do
    refute Year.leap_year?(1987), "1987 is not a leap year."
  end

  test "yet another any old year" do
    refute Year.leap_year?(1487), "1487 is not a leap year."
  end

  test "an even year that is not a leap year" do
    refute Year.leap_year?(1998), "1998 is not a leap year."
  end

  @tag :pending
  test "century" do
    refute Year.leap_year?(1900), "1900 is not a leap year."
  end

  @tag :pending
  test "exceptional century" do
    assert Year.leap_year?(2400)
  end
end
