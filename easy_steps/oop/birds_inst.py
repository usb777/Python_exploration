class Bird :

	'''A base class to define bird properties.'''

	count = 0
	voice = "quick quick"

	def __init__( self ) :

		print("hello world")

	def talk1( self, voice ) :

		return self.voice

	def talk2( self, voice ) :

		return voice   
	    
      
	


bird = Bird()

print("voice = "+bird.talk1("hello"))  # took voice from class
print("voice = "+bird.talk2("voice param"))
#print("voice = "+bird.talk3("hello"))



