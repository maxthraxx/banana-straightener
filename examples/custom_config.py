"""
Custom configuration example for Banana Straightener.

This script demonstrates how to customize every aspect of
the Banana Straightener's behavior through configuration.
"""

import os
from pathlib import Path
from banana_straightener import BananaStraightener, Config

def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Please set your GEMINI_API_KEY")
        print("💡 Method 1 (recommended): echo 'GEMINI_API_KEY=your-key-here' > .env")
        print("💡 Method 2: export GEMINI_API_KEY='your-key-here'")
        return
    
    print("🍌 Custom Configuration Example")
    print("="*50)
    
    # Example 1: High-quality, thorough configuration
    print("🎯 Configuration 1: High-Quality Mode")
    high_quality_config = Config(
        # Model settings
        generator_model="gemini-2.5-flash",
        evaluator_model="gemini-2.5-flash",
        
        # Generation settings
        default_max_iterations=15,       # More attempts
        success_threshold=0.95,          # Very high quality bar
        save_intermediates=True,         # Save all steps
        
        # Output settings  
        output_dir=Path("./high_quality_outputs"),
        
        # Custom evaluation template for higher standards
        evaluation_prompt_template="""
        Analyze this image against the target: "{target_prompt}"
        
        Evaluate with HIGH STANDARDS:
        1. MATCH: Does it PERFECTLY match? (YES/NO)
        2. CONFIDENCE: Rate 0.0-1.0 (be strict, 0.9+ only for excellent)
        3. CORRECT_ELEMENTS: What's done well?
        4. MISSING_ELEMENTS: What's missing or wrong?
        5. IMPROVEMENTS: Specific, detailed improvements needed
        
        Be critical and demand excellence.
        
        MATCH: [YES/NO]
        CONFIDENCE: [0.0-1.0]
        CORRECT_ELEMENTS: [detailed list]
        MISSING_ELEMENTS: [detailed list]
        IMPROVEMENTS: [very specific feedback]
        """
    )
    
    agent1 = BananaStraightener(high_quality_config)
    
    prompt1 = "a photorealistic portrait of an elderly wizard with twinkling eyes"
    print(f"📝 Prompt: {prompt1}")
    print(f"⚙️ Max iterations: {high_quality_config.default_max_iterations}")
    print(f"🎯 Success threshold: {high_quality_config.success_threshold:.0%}")
    
    result1 = agent1.straighten(prompt1)
    print(f"Result: {'Success' if result1['success'] else 'Partial'}")
    print(f"Quality: {result1.get('confidence', result1.get('best_confidence', 0)):.1%}")
    print()
    
    # Example 2: Fast, experimental configuration  
    print("⚡ Configuration 2: Fast Experimental Mode")
    fast_config = Config(
        # Speed-optimized settings
        default_max_iterations=3,        # Quick attempts
        success_threshold=0.65,          # Lower bar for experimentation
        save_intermediates=False,        # Don't save steps
        
        # Output settings
        output_dir=Path("./fast_experiments"),
        
        # Relaxed evaluation for creative exploration
        evaluation_prompt_template="""
        Quick evaluation for: "{target_prompt}"
        
        1. MATCH: Is this in the right direction? (YES/NO)
        2. CONFIDENCE: Rate 0.0-1.0 (be generous for creative attempts)
        3. IMPROVEMENTS: Quick suggestions for next iteration
        
        MATCH: [YES/NO]  
        CONFIDENCE: [0.0-1.0]
        IMPROVEMENTS: [brief feedback]
        """
    )
    
    agent2 = BananaStraightener(fast_config)
    
    prompt2 = "abstract art representing the sound of jazz music"
    print(f"📝 Prompt: {prompt2}")
    print(f"⚙️ Max iterations: {fast_config.default_max_iterations}")
    print(f"🎯 Success threshold: {fast_config.success_threshold:.0%}")
    
    result2 = agent2.straighten(prompt2)
    print(f"Result: {'Success' if result2['success'] else 'Partial'}")
    print(f"Quality: {result2.get('confidence', result2.get('best_confidence', 0)):.1%}")
    print()
    
    # Example 3: Domain-specific configuration
    print("🎨 Configuration 3: Art-Focused Mode")
    art_config = Config(
        default_max_iterations=8,
        success_threshold=0.85,
        save_intermediates=True,
        output_dir=Path("./art_outputs"),
        
        # Art-focused evaluation
        evaluation_prompt_template="""
        Art critique for: "{target_prompt}"
        
        Evaluate as an art critic:
        1. MATCH: Does this fulfill the artistic vision? (YES/NO)
        2. CONFIDENCE: Artistic quality and vision match 0.0-1.0
        3. COMPOSITION: How's the composition and visual balance?
        4. STYLE: Does the style match what was requested?
        5. EMOTION: Does it convey the right mood/feeling?
        6. IMPROVEMENTS: Artistic suggestions for enhancement
        
        MATCH: [YES/NO]
        CONFIDENCE: [0.0-1.0]  
        CORRECT_ELEMENTS: [artistic strengths]
        MISSING_ELEMENTS: [artistic weaknesses]
        IMPROVEMENTS: [artistic direction for next iteration]
        """
    )
    
    agent3 = BananaStraightener(art_config)
    
    prompt3 = "impressionist painting of a garden at twilight with soft purple light"
    print(f"📝 Prompt: {prompt3}")
    
    result3 = agent3.straighten(prompt3)
    print(f"Result: {'Success' if result3['success'] else 'Partial'}")
    print(f"Quality: {result3.get('confidence', result3.get('best_confidence', 0)):.1%}")
    print()
    
    # Example 4: Configuration from environment variables
    print("🌍 Configuration 4: Environment-Based Config")
    
    # Set some environment variables for demonstration
    os.environ.update({
        'MAX_ITERATIONS': '6',
        'SUCCESS_THRESHOLD': '0.80', 
        'SAVE_INTERMEDIATES': 'true',
        'OUTPUT_DIR': './env_outputs'
    })
    
    env_config = Config.from_env()
    print(f"📊 Loaded from environment:")
    print(f"   Max iterations: {env_config.default_max_iterations}")
    print(f"   Success threshold: {env_config.success_threshold:.0%}")
    print(f"   Save intermediates: {env_config.save_intermediates}")
    print(f"   Output dir: {env_config.output_dir}")
    
    agent4 = BananaStraightener(env_config)
    
    prompt4 = "a minimalist logo design for a tech startup"
    result4 = agent4.straighten(prompt4)
    print(f"Environment-based result: {'Success' if result4['success'] else 'Partial'}")
    print()
    
    # Summary
    print("="*50)
    print("📋 CONFIGURATION COMPARISON SUMMARY")
    print("="*50)
    
    configs = [
        ("High-Quality", high_quality_config, result1),
        ("Fast Experimental", fast_config, result2), 
        ("Art-Focused", art_config, result3),
        ("Environment-Based", env_config, result4)
    ]
    
    for name, config, result in configs:
        success = result['success']
        confidence = result.get('confidence', result.get('best_confidence', 0))
        iterations_used = result['iterations']
        max_iterations = config.default_max_iterations
        
        print(f"{name:18} | {confidence:5.1%} | {iterations_used}/{max_iterations} iter | {'✅' if success else '⚠️'}")
    
    print("\n💡 Key Takeaways:")
    print("• High-quality configs get better results but take longer")
    print("• Fast configs are great for experimentation and iteration")  
    print("• Domain-specific configs can improve relevance")
    print("• Environment configs make deployment easier")
    print("\n✅ Custom configuration example complete!")

if __name__ == "__main__":
    main()