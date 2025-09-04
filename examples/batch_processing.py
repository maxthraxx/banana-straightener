"""
Batch processing example for Banana Straightener.

This script shows how to process multiple prompts efficiently,
with progress tracking and result summary.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from banana_straightener import BananaStraightener, Config

def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Please set your GEMINI_API_KEY")
        print("💡 Method 1 (recommended): echo 'GEMINI_API_KEY=your-key-here' > .env")
        print("💡 Method 2: export GEMINI_API_KEY='your-key-here'")
        return
    
    print("🍌 Batch Processing Example")
    print("="*50)
    
    # Prompts to process
    prompts = [
        "a red sports car on a mountain road at sunset",
        "a cat wearing sunglasses sitting on a beach chair", 
        "abstract geometric patterns in blue and gold",
        "a cozy cabin in a snowy forest with smoke from chimney",
        "a robot chef cooking in a futuristic kitchen",
        "a lighthouse on a rocky cliff during a storm",
        "a field of sunflowers under a starry night sky",
    ]
    
    print(f"📋 Processing {len(prompts)} prompts")
    print(f"🎯 Target: 3 iterations each for speed")
    print()
    
    # Configure for batch processing (faster settings)
    config = Config(
        default_max_iterations=3,  # Fewer iterations for speed
        success_threshold=0.75,    # Lower threshold for speed
        save_intermediates=False,  # Don't save intermediate steps
        output_dir=Path("./batch_outputs")
    )
    
    agent = BananaStraightener(config)
    
    # Track results
    results = []
    successful = 0
    total_iterations = 0
    start_time = datetime.now()
    
    # Process each prompt
    for i, prompt in enumerate(prompts, 1):
        print(f"🔄 [{i}/{len(prompts)}] Processing: {prompt[:60]}...")
        
        try:
            result = agent.straighten(
                prompt=prompt,
                max_iterations=3,
                success_threshold=0.75
            )
            
            # Track statistics
            if result['success']:
                successful += 1
                status = "✅ Success"
                confidence = result['confidence']
            else:
                status = "⚠️ Partial"
                confidence = result['best_confidence']
            
            total_iterations += result['iterations']
            
            print(f"    {status} | {confidence:.1%} confidence | {result['iterations']} iterations")
            
            # Store result summary
            results.append({
                'prompt': prompt,
                'success': result['success'],
                'confidence': confidence,
                'iterations': result['iterations'],
                'image_path': result.get('final_image_path'),
                'session_dir': result['session_dir']
            })
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            results.append({
                'prompt': prompt,
                'success': False,
                'confidence': 0.0,
                'iterations': 0,
                'error': str(e)
            })
        
        print()
    
    # Calculate statistics
    end_time = datetime.now()
    duration = end_time - start_time
    success_rate = successful / len(prompts)
    avg_iterations = total_iterations / len(prompts)
    
    # Display summary
    print("="*60)
    print("📊 BATCH PROCESSING SUMMARY")
    print("="*60)
    print(f"Total prompts: {len(prompts)}")
    print(f"Successful: {successful} ({success_rate:.1%})")
    print(f"Average iterations: {avg_iterations:.1f}")
    print(f"Total time: {duration.total_seconds():.1f} seconds")
    print(f"Average time per prompt: {duration.total_seconds() / len(prompts):.1f} seconds")
    print()
    
    # Show detailed results
    print("📋 DETAILED RESULTS:")
    print("-" * 60)
    
    for i, result in enumerate(results, 1):
        status = "✅" if result['success'] else ("❌" if 'error' in result else "⚠️")
        confidence = result.get('confidence', 0)
        iterations = result.get('iterations', 0)
        
        print(f"{i:2d}. {status} {confidence:5.1%} | {iterations} iter | {result['prompt'][:45]}")
    
    # Save batch report
    report_path = config.output_dir / f"batch_report_{start_time.strftime('%Y%m%d_%H%M%S')}.json"
    batch_report = {
        'timestamp': start_time.isoformat(),
        'duration_seconds': duration.total_seconds(),
        'total_prompts': len(prompts),
        'successful': successful,
        'success_rate': success_rate,
        'average_iterations': avg_iterations,
        'results': results
    }
    
    try:
        with open(report_path, 'w') as f:
            json.dump(batch_report, f, indent=2, default=str)
        print(f"\n💾 Batch report saved: {report_path}")
    except Exception as e:
        print(f"⚠️ Could not save batch report: {e}")
    
    # Show top performers
    successful_results = [r for r in results if r['success']]
    if successful_results:
        print("\n🏆 TOP PERFORMERS:")
        top_results = sorted(successful_results, key=lambda x: x['confidence'], reverse=True)[:3]
        for i, result in enumerate(top_results, 1):
            print(f"  {i}. {result['confidence']:.1%} - {result['prompt'][:50]}")
    
    print(f"\n📂 All outputs saved to: {config.output_dir}")
    print("✅ Batch processing complete!")

if __name__ == "__main__":
    main()