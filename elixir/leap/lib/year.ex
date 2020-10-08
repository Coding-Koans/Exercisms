defmodule Year do

  def leap_year?(year) do
    if rem(year, 4) == 0 do
      true
    else
      false
    end
  end
end
