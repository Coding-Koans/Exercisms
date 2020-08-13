class Hamming
  def self.compute strand_1, strand_2
    throw ArgumentError unless strand_1.length == strand_2.length
    
    hamming_count = 0
    strand_1.split('').each_with_index do |this_nucelic_acid, index|
      that_nucleic_acid = strand_2[index]
      hamming_count += 1 unless this_nucelic_acid == that_nucleic_acid
    end 
    
    hamming_count
  end
end

module BookKeeping
 VERSION = 3
end

#Paired solution with Anuj More! @execat
#Paired with Gary too. Also twitch.tv/outpost13