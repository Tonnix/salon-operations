var CapacityRules = Object.freeze({
  overlaps: function(a,b) { return a.start < b.end && b.start < a.end; },
  stylingReady: function(x) { return x.confirmed === true && x.glueComplete === true && x.safeSettingComplete === true && Number.isFinite(x.glueStart) && Number.isFinite(x.now) && x.now >= x.glueStart + 30*60000; }
});
