class StringUtil:
      @staticmethod
      def reverse_string(input_str):
          return input_str[::-1]

      @staticmethod
      def capitalize_string(input_str):
          return input_str.upper()

      @staticmethod
      def lowercase_string(input_str):
          return input_str.lower()

def test_reverse_string():
    string = "aBc"
    
    #reversed string
    result = StringUtil.reverse_string(string)
    
    # This test will succeed
    assert result == "cBa"

    #Test will fail.
    #assert result == "cBA" 

def test_capitalize_string():
      string = "aBc"
    
    #Capitalize string
      result = StringUtil.capitalize_string(string)
      
      # This test will succeed
      assert result == "ABC"

      # This test will fail
      #assert result == "ACB"

def test_lowercase_string():
      string = "aBc"
      
      # Lowercase string
      result = StringUtil.lowercase_string(string)
      
      # This test will succeed
      assert result == "abc"

      # This test will fail
      # assert result == "acb"



  # Run the tests
if __name__ == "__main__":
      test_reverse_string()
      test_capitalize_string()
      test_lowercase_string()

      print("All tests passed successfully!")