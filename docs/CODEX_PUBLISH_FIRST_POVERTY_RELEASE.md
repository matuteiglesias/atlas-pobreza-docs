# Codex work packet — publish the first inspectable poverty release

## Mission

Turn this documentation repository into a static, read-only presentation surface
for one copied immutable poverty release.

The Atlas must never calculate poverty, run models, sample Census data, fetch
mutable upstream branches or silently replace indicator values. It consumes a
release already produced and verified by `indice-pobreza-UBA`.

The first published surface may display a synthetic or legacy-candidate release,
but its status and limitations must be unmistakable.

## Read first

Inspect:

- `README.md`, `SYSTEM.yaml` and `DEPLOYMENT_STATUS.md`;
- `scripts/verify_deployment_config.py` and the bounded deployment-repair packet;
- Docusaurus configuration, routes, existing pages and static assets;
- the output manifest and release-inspection contract from `indice-pobreza-UBA`;
- the exact copied release directory supplied for this task.

Do not infer data from screenshots or old Atlas pages.

# Part A — repair the truthful static-site boundary

Remove remaining starter metadata only after selecting explicit project values.

The site must declare:

- title and description for the Argentina poverty research Atlas;
- owning repository and documentation authority;
- release status banner (`synthetic`, `legacy_candidate`, `candidate`, `approved`);
- release ID, period and verification state;
- explicit statement that it is not an official INDEC poverty publication;
- a stable local build command;
- one explicit deployment destination when configured.

Make `scripts/verify_deployment_config.py` green only when every placeholder and
example identity has been replaced truthfully.

# Part B — immutable data intake

Add a local import/build command such as:

```bash
npm run import-release -- /copied/poverty-release-dir
```

or an equivalent repository-native command.

The importer must:

- validate the poverty release checksums before reading tables;
- reject mutable URLs, `latest`, unsafe paths and missing manifests;
- copy only public-safe release outputs into a content-addressed static directory;
- never reach into a sibling checkout at site runtime;
- record the source release manifest hash and producer commit;
- refuse to overwrite an existing release ID with different bytes;
- keep multiple releases separately addressable when desired.

Do not copy raw Census persons, household microdata or person-level predictions
into the public site.

Allowed public inputs should be limited to:

```text
national_summary
department_summary
aggregates_tidy
department_spatial
pre-rendered plots
release manifest
QA summary
limitations
```

# Part C — first visible pages

Create a compact release-oriented surface.

## C1. Release overview

Show:

- release ID and status;
- period;
- direct input release identities;
- methodology/policy summary;
- national household and person poverty/indigence rates;
- coverage and weight policy;
- prominent limitations.

## C2. Department table

Provide a sortable/filterable table with:

- department ID and name when available;
- household poverty rate;
- household indigence rate;
- person poverty rate;
- person indigence rate;
- weighted numerator and denominator;
- coverage;
- release/status link.

Do not rank departments when denominators or coverage are not comparable without
showing the relevant warning.

## C3. Maps

Render the supplied CPV-2010 department GeoJSON locally in the browser or as a
static build artifact.

Support at least:

- household poverty rate;
- household indigence rate;
- person poverty rate;
- person indigence rate.

The map must:

- display missing values distinctly;
- expose the geography vintage;
- use the exact release values without recalculation;
- include a legend and data-status note;
- never load Mapbox credentials for the initial publication.

Prefer a lightweight open-source/static map approach. Remote tile publication is
out of scope for the first release.

## C4. Plots and diagnostics

Display or generate from aggregate tables only:

- national household/person rate comparison;
- ranked department rates;
- poverty versus indigence scatter or paired plot;
- denominator/coverage diagnostic;
- any pre-rendered release plots supplied by the producer.

The site may transform values into display percentages, but it must not change
scientific definitions or aggregate microdata.

## C5. Method and limitations

Publish human-readable pages explaining:

- Census sample frame and period interpretation;
- modeled income status;
- adult-equivalence and basket release identities;
- price/monetary reference;
- threshold and gap policies;
- weighting/estimand policy;
- geography vintage;
- unresolved warnings;
- the distinction between research output and official poverty statistics.

# Part D — static release index

Create a machine-readable static release index containing:

```text
release_id
status
period
manifest_sha256
producer_commit
national summary path
department table path
GeoJSON path
plot paths
limitations path
import/build verification status
```

The homepage should resolve an explicitly configured default release. Do not use a
floating `latest` alias internally; a human-readable “current displayed release”
may point to an immutable ID.

# Part E — checks and deployment

Provide commands equivalent to:

```bash
npm ci
npm run import-release -- /copied/release
npm run validate-data
npm run build
```

Tests must cover:

- checksum failure;
- missing public output role;
- attempted person/household microdata import;
- duplicate release ID with different bytes;
- department table/GeoJSON key mismatch;
- nonfinite aggregate value;
- missing status/limitations;
- deterministic static data build;
- removal of all Docusaurus starter placeholders;
- site build without secrets or networked scientific inputs.

Deployment may be configured after a successful local build. Do not resurrect an
old `gh-pages` artifact as proof that the current source is deployed.

# Progressive publication policy

The site should allow visible progress without misrepresentation:

- `synthetic`: usable to test pages and maps; large status banner;
- `legacy_candidate`: real historical artifacts with incomplete provenance;
- `candidate`: complete governed run with declared research limitations;
- `approved`: only after explicit scientific approval outside this task.

A warning does not hide the release. It is displayed. Corruption, missing
identity or unsafe public data remains a hard failure.

# Non-goals

- No poverty computation.
- No model or Census execution.
- No person-level public data.
- No mutable branch fetches at runtime.
- No Mapbox/GCS credentials or destructive upload.
- No official-statistics claim.
- No automatic scientific approval.

# Acceptance criteria

```text
one immutable poverty release can be imported and verified locally
national and department aggregates are visible
map-ready GeoJSON is rendered without remote credentials
plots are generated from released aggregate tables only
all status and limitations are prominent
starter metadata and red deployment placeholders are repaired truthfully
the site builds deterministically and contains no person-level data
```

# Completion report

The final PR must state:

- release ID imported;
- exact public-safe files copied;
- pages, tables, plots and maps created;
- status and limitations shown;
- commands/tests run;
- local build output;
- deployment status and URL only if actually verified;
- confirmation that no science, model, Census sampling or person-level publication occurred.
