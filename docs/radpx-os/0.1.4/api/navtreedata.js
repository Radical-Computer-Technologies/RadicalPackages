/*
 @licstart  The following is the entire license notice for the JavaScript code in this file.

 The MIT License (MIT)

 Copyright (C) 1997-2020 by Dimitri van Heesch

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software
 and associated documentation files (the "Software"), to deal in the Software without restriction,
 including without limitation the rights to use, copy, modify, merge, publish, distribute,
 sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or
 substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 @licend  The above is the entire license notice for the JavaScript code in this file
*/
var NAVTREE =
[
  [ "RADPx-OS Kernel (Radical Posix OS)", "index.html", [
    [ "RADPx-OS Kernel API", "index.html", [
      [ "Start Here", "index.html#autotoc_md43", null ],
      [ "API Groups", "index.html#autotoc_md44", null ],
      [ "Filesystem and Package Profile", "index.html#autotoc_md45", null ],
      [ "Verification", "index.html#autotoc_md46", null ]
    ] ],
    [ "RADPx-OS Platform Layout", "md__media_jvincent_Kingspec512_repos_RADPx_OS_RADKernel_platforms_README.html", null ],
    [ "RADPx-OS x86_64 Platform", "md__media_jvincent_Kingspec512_repos_RADPx_OS_RADKernel_platforms_x86_64_README.html", null ],
    [ "API Groups", "api_groups.html", [
      [ "Kernel And Boot", "api_groups.html#autotoc_md2", null ],
      [ "Time, Tasks, And Synchronization", "api_groups.html#autotoc_md3", null ],
      [ "POSIX-Inspired Runtime", "api_groups.html#autotoc_md4", null ],
      [ "Device Model", "api_groups.html#autotoc_md5", null ],
      [ "Networking", "api_groups.html#autotoc_md6", null ],
      [ "Driver Binding", "api_groups.html#autotoc_md7", null ],
      [ "Overlay Tree And IRQs", "api_groups.html#autotoc_md8", null ],
      [ "Display And Input", "api_groups.html#autotoc_md9", null ],
      [ "Experimental Compositor", "api_groups.html#autotoc_md10", null ]
    ] ],
    [ "API Structure", "api_structure.html", [
      [ "Initialization And Boot", "api_structure.html#autotoc_md11", null ],
      [ "Runtime Services", "api_structure.html#autotoc_md12", null ],
      [ "Platform Layout", "api_structure.html#autotoc_md13", null ],
      [ "Handle Rules", "api_structure.html#autotoc_md14", null ],
      [ "Crimson Stability", "api_structure.html#autotoc_md15", null ]
    ] ],
    [ "Architecture & Layout", "architecture.html", [
      [ "Design shape", "architecture.html#autotoc_md16", null ],
      [ "The <tt>RADKernel/</tt> tree", "architecture.html#autotoc_md17", null ],
      [ "Everything else", "architecture.html#autotoc_md18", null ],
      [ "How a target is assembled", "architecture.html#autotoc_md19", null ]
    ] ],
    [ "Crimson 0.1.4 Status", "crimson_status.html", [
      [ "Stable-Beta Surface", "crimson_status.html#autotoc_md20", null ],
      [ "Experimental Surface", "crimson_status.html#autotoc_md21", null ],
      [ "Not Yet Complete", "crimson_status.html#autotoc_md22", null ]
    ] ],
    [ "Overlay And Device Tree Guide", "device_tree_guide.html", [
      [ "Overlay Shape", "device_tree_guide.html#autotoc_md23", null ],
      [ "Bus And Device Binding", "device_tree_guide.html#autotoc_md24", null ],
      [ "Interrupt Domains", "device_tree_guide.html#autotoc_md25", null ],
      [ "Framebuffer Outputs", "device_tree_guide.html#autotoc_md26", null ],
      [ "Boot Services", "device_tree_guide.html#autotoc_md27", null ],
      [ "Current Limits", "device_tree_guide.html#autotoc_md28", null ]
    ] ],
    [ "Minimal Examples", "minimal_examples.html", [
      [ "Register A Kernel Module", "minimal_examples.html#autotoc_md29", null ],
      [ "Register An I2C Controller And Child Driver", "minimal_examples.html#autotoc_md30", null ],
      [ "Register DMA And Use SPI Auto Mode", "minimal_examples.html#autotoc_md31", null ],
      [ "Register A Framebuffer", "minimal_examples.html#autotoc_md32", null ],
      [ "Read Input Events", "minimal_examples.html#autotoc_md33", null ],
      [ "Mount A VFS Provider", "minimal_examples.html#autotoc_md34", null ],
      [ "Use File Descriptors Through The Syscall ABI", "minimal_examples.html#autotoc_md35", null ]
    ] ],
    [ "Getting Started", "getting_started.html", [
      [ "What you are building", "getting_started.html#autotoc_md36", null ],
      [ "Prerequisites", "getting_started.html#autotoc_md37", null ],
      [ "1. Prove the core builds (host tests, ~1 minute)", "getting_started.html#autotoc_md38", null ],
      [ "2. Boot the x86_64 terminal (ISO, ~2–3 minutes)", "getting_started.html#autotoc_md39", null ],
      [ "3. Boot the ZuBoard-1CG in QEMU (A53, ~2–3 minutes)", "getting_started.html#autotoc_md40", null ],
      [ "Where to go next", "getting_started.html#autotoc_md41", null ]
    ] ],
    [ "Experimental Networking", "networking.html", [
      [ "Current Stack", "networking.html#autotoc_md47", null ],
      [ "Current Limits", "networking.html#autotoc_md48", null ],
      [ "Verification", "networking.html#autotoc_md49", null ]
    ] ],
    [ "Pi Zero 2 W Bring-Up", "pi_zero2w.html", [
      [ "Required Loader State", "pi_zero2w.html#autotoc_md50", null ],
      [ "Current Payload", "pi_zero2w.html#autotoc_md51", null ],
      [ "Circle Loader Gate", "pi_zero2w.html#autotoc_md52", null ],
      [ "Current Limits", "pi_zero2w.html#autotoc_md53", null ]
    ] ],
    [ "RadBuild Integration", "radbuild_integration.html", [
      [ "Build Command", "radbuild_integration.html#autotoc_md54", null ],
      [ "Artifact Output", "radbuild_integration.html#autotoc_md55", null ],
      [ "rkconfig and Root Filesystem Layout", "radbuild_integration.html#autotoc_md56", null ],
      [ "Publication and Packagegroups", "radbuild_integration.html#autotoc_md57", null ]
    ] ],
    [ "RADCompositor", "radcompositor.html", [
      [ "Architecture", "radcompositor.html#autotoc_md58", null ],
      [ "Shared-Memory IPC", "radcompositor.html#autotoc_md59", null ],
      [ "Current Limits", "radcompositor.html#autotoc_md60", null ],
      [ "Verification", "radcompositor.html#autotoc_md61", null ]
    ] ],
    [ "ZuBoard 1CG A53 Handoff Status", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg_handoff.html", [
      [ "What Works", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg_handoff.html#autotoc_md63", null ],
      [ "Verified Marker Path", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg_handoff.html#autotoc_md64", null ],
      [ "Current Blocker", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg_handoff.html#autotoc_md65", null ],
      [ "Recommended Next Steps", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg_handoff.html#autotoc_md66", null ]
    ] ],
    [ "ZuBoard 1CG Serial Bring-Up", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg.html", [
      [ "Boot Model", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg.html#autotoc_md68", null ],
      [ "Current Kernel Scope", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg.html#autotoc_md69", null ],
      [ "Build", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg.html#autotoc_md70", null ],
      [ "QEMU Smoke", "md__media_jvincent_Kingspec512_repos_RADPx_OS_docs_public_zuboard_1cg.html#autotoc_md71", null ]
    ] ],
    [ "Classes", "annotated.html", [
      [ "Class List", "annotated.html", "annotated_dup" ],
      [ "Class Index", "classes.html", null ],
      [ "Class Members", "functions.html", [
        [ "All", "functions.html", "functions_dup" ],
        [ "Functions", "functions_func.html", null ],
        [ "Variables", "functions_vars.html", "functions_vars" ]
      ] ]
    ] ],
    [ "Files", "files.html", [
      [ "File List", "files.html", "files_dup" ],
      [ "File Members", "globals.html", [
        [ "All", "globals.html", "globals_dup" ],
        [ "Functions", "globals_func.html", "globals_func" ],
        [ "Typedefs", "globals_type.html", null ],
        [ "Enumerations", "globals_enum.html", null ],
        [ "Enumerator", "globals_eval.html", "globals_eval" ],
        [ "Macros", "globals_defs.html", null ]
      ] ]
    ] ]
  ] ]
];

var NAVTREEINDEX =
[
"a53__parity__selftest_8h_source.html",
"radbuild_integration.html#autotoc_md54",
"radkernel_8h.html#a5a4249cecdfe8ab58425c9aa2d7b9a69",
"radkernel_8h.html#aa02986f24b8df7c531767da0e3750177",
"radkernel_8h.html#adf7bbeb23054ca24451821557c27e1a2af773b2e5252c8fc9918e986bf13a187c",
"structrad__display__mode.html#ad5bc39bc4a473ecf7362590931a11cf3",
"structrad__process__arch__ops.html#a84bde395ce45e1a0d1908b020d6219dc",
"structx86__storage__summary.html#a5d5bac3ab9a74097c1532a27e1186f50"
];

var SYNCONMSG = 'click to disable panel synchronisation';
var SYNCOFFMSG = 'click to enable panel synchronisation';