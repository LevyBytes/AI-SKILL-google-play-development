## Publishing large apps and games on Google Play

### What are Google Play app size limits when using AABs?

The maximum compressed download size for a base module generated from an AAB is 500 MB. That is, Google Play will first generate the base module, then any additional feature modules or asset packs from your AAB. Next, Google Play checks that the maximum cumulative total compressed download size that any individual device receives is not over 4 GB.

### Does Google Play support expansion files (OBBs) for AABs?

No, Google Play does not support expansion files for AABs. Expansion files (OBBs) are a legacy Google Play-specific solution for publishing large apps and games using APKs. There are Google and third-party alternatives for AABs larger than 500 MB.

### How do I publish an app or game larger than 500 MB on Google Play?

Large apps and games using AABs can either use Play delivery services such as Play Asset Delivery or Play Feature Delivery to exceed the 500 MB size limit or they can use third-party content delivery networks.

### What benefits does Play Asset Delivery offer over expansion files (OBBs)?

On Google Play, APKs required separate expansion files (OBBs) to serve additional resources to users. However, because OBBs were not signed and are stored in the app's external storage, they're not very secure. With Play Asset Delivery (PAD), games larger than 500 MB can replace OBBs by publishing the entire game as a single app bundle on the Play Store. In addition to offering a smoother publishing process and flexible delivery modes, PAD means updates require less device storage. As a result, it can drive higher install rates.

Finally, with ASTC now supported on ~80% of devices, PAD's texture compression format targeting feature lets you serve ASTC to devices that support it. You can target the widest range of devices while making efficient use of the available hardware and device storage.

## Google Play delivery features unlocked by AABs

### What are examples of new features that Play is offering developers using AABs?

App stores like Google Play process AABs into installable APKs. Being responsible for the APKs makes it possible to offer new features and services that bring benefits to developers and users. Play already offers such services that are already widely used and valued by developers, two examples are [Play Feature Delivery](<https://developer.android.com/guide/playcore/feature-delivery>) and [Play Asset Delivery](<https://developer.android.com/guide/playcore/asset-delivery>).

### What is Play Feature Delivery?

One of the features of app bundles is that they allow separating an app into multiple modules, called "feature modules". These modules can then be dynamically delivered to users and devices at different times (unlike in the past when everything had to be delivered as one file at install time). Play Feature Delivery gives you the ability to customize what feature modules are delivered to which device and when, with install-time, conditional, and on-demand delivery modes. This lets you reduce your app size, leading to more installs, and tailor your app experience. For example, you could deliver a rarely used feature like customer support on-demand to the users who need it instead of at install time, reducing the size of your initial install for all users. Or you could deliver your complete app experience to high-end devices while delivering a smaller app experience with optional, on-demand features to entry-level devices that have data and device storage constraints.

### What is Play Asset Delivery?

Play Asset Delivery allows game developers to improve the user experience and reduce user waiting time by dynamically delivering large assets at the optimal time. Games using Play Asset Delivery can also make use of texture compression format targeting, so your users only get the assets suitable for their device, with no wasted space or bandwidth.

### Are these Play delivery features available on other app stores?

No, Play Feature Delivery and Play Asset Delivery involve apps and games directly interfacing with the Google Play Store. These optional services are examples of Play differentiating itself as an app store and bringing additional value and usefulness to Play developers and users. Other app stores using app bundles and APKs offer their own app store services to developers.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/faq).
