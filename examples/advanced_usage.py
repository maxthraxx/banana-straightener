"""
Advanced usage example for Banana Straightener.

This script demonstrates advanced features like:
- Custom configuration
- Input image modification  
- Real-time iteration monitoring
- Custom callback functions
- Error handling
"""

import os
from pathlib import Path
from PIL import Image
from banana_straightener import BananaStraightener, Config

def iteration_callback(iteration, image, evaluation):
    """Custom callback to monitor each iteration."""
    print(f"  🔄 Iteration {iteration}")
    print(f"     Match: {'✅' if evaluation['matches_intent'] else '❌'}")
    print(f"     Confidence: {evaluation['confidence']:.1%}")
    if not evaluation['matches_intent']:
        improvements = evaluation['improvements'][:100]
        print(f"     Next: {improvements}...")
    print()

def main():
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Please set your GEMINI_API_KEY")
        print("💡 Method 1 (recommended): echo 'GEMINI_API_KEY=your-key-here' > .env")
        print("💡 Method 2: export GEMINI_API_KEY='your-key-here'")
        return
    
    print("🍌 Advanced Banana Straightener Example")
    print("="*60)
    
    # Custom configuration
    config = Config(
        default_max_iterations=8,        # More iterations
        success_threshold=0.90,          # Higher quality bar
        save_intermediates=True,         # Save all steps
        output_dir=Path("./advanced_outputs")
    )
    
    print(f"⚙️ Configuration:")
    print(f"   Max iterations: {config.default_max_iterations}")
    print(f"   Success threshold: {config.success_threshold:.0%}")
    print(f"   Output directory: {config.output_dir}")
    print()
    
    # Initialize agent
    agent = BananaStraightener(config)
    
    # Example 1: Generate from scratch with high quality
    print("🎨 Example 1: High-quality generation")
    prompt1 = "a majestic dragon reading a book in a cozy library, oil painting style"
    print(f"📝 Prompt: {prompt1}")
    
    result1 = agent.straighten(
        prompt=prompt1,
        max_iterations=6,
        success_threshold=0.88,
        callback=iteration_callback
    )
    
    print(f"Result 1: {'Success' if result1['success'] else 'Partial'}")
    print(f"Final confidence: {result1.get('confidence', result1.get('best_confidence', 0)):.1%}")
    print()
    
    # Example 2: Real-time iteration processing
    print("🔄 Example 2: Real-time iteration monitoring")
    prompt2 = "a steampunk robot tending a garden of mechanical flowers"
    print(f"📝 Prompt: {prompt2}")
    
    iteration_count = 0
    best_confidence = 0.0
    final_image = None
    
    for iteration_data in agent.straighten_iterative(
        prompt=prompt2,
        max_iterations=5,
        success_threshold=0.85
    ):
        iteration_count = iteration_data['iteration']
        confidence = iteration_data['evaluation']['confidence']
        
        print(f"  🔄 Live update - Iteration {iteration_count}")
        print(f"     Confidence: {confidence:.1%}")
        
        if confidence > best_confidence:
            best_confidence = confidence
            final_image = iteration_data['current_image']
        
        if iteration_data['success']:
            print(f"  🎉 Success achieved!")
            break
        
        print(f"     Next: {iteration_data['evaluation']['improvements'][:80]}...")
        print()
    
    if final_image:
        final_image.save("advanced_example_result.png")
        print(f"💾 Saved best result: advanced_example_result.png")
    
    # Example 3: Image modification (if you have an input image)
    sample_image_path = "input_sample.jpg"
    if os.path.exists(sample_image_path):
        print("\n🖼️ Example 3: Image modification")
        print(f"📁 Loading: {sample_image_path}")
        
        input_image = Image.open(sample_image_path)
        
        modification_prompt = "make this image look like a watercolor painting"
        print(f"📝 Modification: {modification_prompt}")
        
        result3 = agent.straighten(
            prompt=modification_prompt,
            input_image=input_image,
            max_iterations=5,
            callback=iteration_callback
        )
        
        if result3['success']:
            print(f"🎉 Successfully modified image!")
        
        print(f"Result saved to: {result3['session_dir']}")
    else:
        print(f"\n💡 To try image modification, place an image at '{sample_image_path}'")
    
    # Example 4: Error handling
    print("\n🛡️ Example 4: Error handling")
    try:
        # This might fail due to rate limits or other issues
        stress_test_result = agent.straighten(
            prompt="extremely complex surreal abstract art with impossible geometry",
            max_iterations=2  # Low iterations for testing
        )
        print("Stress test completed successfully!")
        
    except Exception as e:
        print(f"⚠️ Handled error gracefully: {e}")
        print("This is normal - the system is robust to API issues.")
    
    print("\n✅ Advanced example complete!")
    print(f"🗂️ Check your outputs in: {config.output_dir}")

if __name__ == "__main__":
    main()