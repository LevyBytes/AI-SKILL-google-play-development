### Unreal Engine

The following sections describe how to integrate and set up the Google Play Integrity API for Unreal Engine projects.

#### Supported Unreal Engine versions

The plugin supports **Unreal Engine 5.0** and all subsequent versions.

#### Set up your development environment

> **Note:** If you have already used the In-app Reviews or In-app Updates plugins in Unreal Engine, you can skip to the final step.

1. Download the [Play Unreal Engine Plugin](<https://github.com/google/play-unreal-engine-plugin>) from the GitHub repository.
2. Copy the `GooglePlay` folder inside your `Plugins` folder in your Unreal Engine project.
3. Open your Unreal Engine project and click **Edit → Plugins**.
4. Search for **Google Play** and check the **Enabled** checkbox.
5. Restart the game project and trigger a build.
6. Open your project's `Build.cs` file and add the `PlayIntegrity` module to `PublicDependencyModuleNames`:

   ```c#
   using UnrealBuildTool;

   public class MyGame : ModuleRules
   {
     public MyGame(ReadOnlyTargetRules Target) : base(Target)
     {
       // ...

       PublicDependencyModuleNames.Add("PlayIntegrity");

       // ...
     }
   }
   ```

### Native

Follow the [native setup guide](<https://developer.android.com/google/play/integrity/native-setup>). For more details, see Play Integrity's [native API reference documentation](<https://developer.android.com/reference/native/play/core/group/integrity>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/setup).
