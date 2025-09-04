"""
Basic usage example for Banana Straightener.

This script shows the simplest way to use Banana Straightener
to generate and improve images iteratively.
"""

import os
from banana_straightener import BananaStraightener

def main():
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Please set your GEMINI_API_KEY")
        print("💡 Get your key from: https://aistudio.google.com/app/apikey")
        print("💡 Method 1 (recommended): echo 'GEMINI_API_KEY=your-key-here' > .env")
        print("💡 Method 2: export GEMINI_API_KEY='your-key-here'")
        return
    
    print("🍌 Basic Banana Straightener Example")
    print("="*50)
    
    # Initialize the agent with default settings
    agent = BananaStraightener()
    
    # Simple prompt
    prompt = "a perfectly straight banana on a white background"
    print(f"📝 Prompt: {prompt}")
    print()
    
    # Run the straightening process
    result = agent.straighten(prompt)
    
    # Check results
    if result['success']:
        print(f"🎉 Success! Generated perfect image in {result['iterations']} iterations")
        print(f"📊 Final confidence: {result['confidence']:.1%}")
        print(f"💾 Saved to: {result['final_image_path']}")
        
        # Save with a custom name too
        result['final_image'].save('my_perfect_banana.png')
        print("💾 Also saved as: my_perfect_banana.png")
        
    else:
        print(f"⚠️ Reached max iterations without perfect success")
        print(f"📊 Best confidence: {result['best_confidence']:.1%}")
        print(f"💾 Best attempt saved to: {result['final_image_path']}")
        print(f"💡 Try increasing iterations or adjusting the prompt")
    
    print(f"\n📂 Full session saved to: {result['session_dir']}")

if __name__ == "__main__":
    main()