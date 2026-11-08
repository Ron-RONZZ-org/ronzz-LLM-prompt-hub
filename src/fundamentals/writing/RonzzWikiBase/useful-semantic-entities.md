### How to use this list

Q-ids are instance-specific. **Never invent a Q-id.** Confirm an entity with `wikibase-search-entities` / `wikibase-get-entity` before reuse; call `embeddable-describe-entity-type` for the authoritative field and class list. The tables below are the classes, vocabularies and properties an LLM editor most often needs.

### 1. Agents and collective classes

Use these as the `instance of` (P1) value, or as `collectiveClass` when creating a collective.

| Entity | Q-id | Use |
| --- | --- | --- |
| person | **Q6** | authors, creators, members |
| organization | **Q7** | generic collective (the default) |
| group of humans | **Q8** | author groups, bands, teams with individual `has member` (P82) Persons |
| fictional character | **Q364** | |
| software | **Q163** | canonical; Q1432 was merged into it — do not recreate Q1432 |
| free and open-source software | **Q179** | |
| publisher | **Q1730** | `collectiveClass` for publishers |
| scholarly journal | **Q1731** | `collectiveClass` for journals and periodicals |
| private company | **Q341** | |
| public company | **Q342** | |
| non-profit organization | **Q343** | |
| governmental agency | **Q344** | |
| music band | **Q345** | |
| educational institution | **Q346** | |
| research institute | **Q347** | |
| political party | **Q348** | |
| trade union | **Q349** | |
| religious organization | **Q350** | |
| sports team | **Q351** | |
| intergovernmental organization | **Q1175** | |

### 2. Citation-source classes

`classKey` is the value passed to `embeddable-add-citation-source`; the Q-id is the class item the Source is classified under.

| `classKey` | Entity | Q-id |
| --- | --- | --- |
| book | book | **Q9** |
| scholarly-article | scholarly article | **Q10** |
| website | website | **Q11** |
| webpage | web page | **Q339** |
| song | song | **Q12** |
| film | film | **Q13** |
| video | video | **Q14** |
| youtube-channel | YouTube channel | **Q337** |
| youtube-video | YouTube video | **Q338** |
| book-excerpt | book excerpt | **Q340** |
| newspaper-article | newspaper article | **Q1714** |
| magazine-article | magazine article | **Q1715** |
| conference-paper | conference paper | **Q1716** |
| report | report | **Q1717** |
| document | document | **Q1718** |
| thesis | thesis | **Q1719** |
| manuscript | manuscript | **Q1720** |
| patent | patent | **Q1721** |
| legal-case | legal case | **Q1722** |
| legislation | legislation | **Q1723** |
| bill | bill | **Q1724** |
| treaty | treaty | **Q1725** |
| interview | interview | **Q1726** |
| map | map | **Q1727** |
| presentation | presentation | **Q1728** |
| dataset | dataset | **Q1729** |
| transcript | transcript | **Q2506** |
| text | text | **Q1735** |
| law | legal provision | **Q2034** |

### 3. Software vocabulary

| Entity | Q-id | Used for |
| --- | --- | --- |
| operating system | **Q301** | `operatingSystem` |
| software license | **Q302** | `license` |
| free software license | **Q1433** | license subclass |
| user interface | **Q303** | `userInterface` |
| programming language | **Q5** | `programmingLanguage` |

### 4. Embedded content and media

| Entity | Q-id | Used for |
| --- | --- | --- |
| quotation content | **Q2** | `embeddable-add-special-content` (`kind=quotation`) |
| code snippet | **Q3** | `…(kind=code-snippet)` |
| mathematical expression | **Q4** | `…(kind=math)` |
| image | **Q488** | the item sitelinked to a `File:` page |

### 5. Common licences

Pass the Q-id as `license` on upload and on image items.

| Licence | Q-id |
| --- | --- |
| CC BY-SA 4.0 | **Q320** (default for our own figures) |
| CC BY 4.0 | **Q319** |
| CC0 1.0 | **Q318** |
| Public domain | **Q610** |
| Proprietary | **Q2726** |
| All rights reserved | **Q2799** (internal-use, copyright-restricted files) |

The full licence label → Q-id map is returned by `embeddable-describe-entity-type(kind='image-facts')`.

### 6. Properties

`datatype` tells you what a value looks like: an **item** value is a Q-id, an **external-id** is the bare identifier, **url** is a full URL, **time** is a date, **quantity** is a number, **monolingualtext** is text plus a language code.

| Property | ID | Datatype | Use |
| --- | --- | --- | --- |
| instance of | **P1** | item | the class of an item |
| attributed to | **P6** | item | author or creator |
| source | **P28** | item | the work an item is cited from |
| part of | **P44** | item | the entity this item is part of or excerpted from |
| source URL | **P7** | url | URL of the cited source |
| date | **P8** | time | publication or creation date |
| content text | **P2** | monolingualtext | quotation payload |
| code source | **P3** | string | code-snippet payload |
| LaTeX source | **P4** | string | math payload |
| programming language | **P5** | item | language of a code snippet |
| describes | **P29** | item | what a math expression describes |
| implementation of | **P30** | item | what a code snippet implements |
| note | **P75** | string | wikitext note on a math item |
| pre-content note | **P79** | string | wikitext note above a math item |
| translation | **P76** | monolingualtext | quotation translation |
| Wikidata ID | **P12** | external-id | |
| ORCID | **P13** | external-id | |
| VIAF ID | **P14** | external-id | |
| ISNI | **P15** | external-id | |
| DOI | **P16** | external-id | |
| ISBN-13 | **P17** | external-id | |
| OpenAlex Work ID | **P18** | external-id | |
| PubMed ID | **P19** | external-id | |
| OpenAlex author ID | **P58** | external-id | |
| YouTube channel ID | **P46** | external-id | |
| YouTube video ID | **P47** | external-id | |
| given name | **P20** | string | person label component |
| family name | **P21** | string | person label component |
| date of birth | **P50** | time | |
| date of death | **P52** | time | |
| place of birth | **P51** | item | |
| place of death | **P53** | item | |
| place of birth (OSM) | **P63** | external-id | `node/…`, `way/…` or `relation/…` |
| place of death (OSM) | **P64** | external-id | `node/…`, `way/…` or `relation/…` |
| place of birth (label) | **P65** | string | display label for P63 |
| place of death (label) | **P66** | string | display label for P64 |
| affiliated with | **P81** | item | organisation a person belongs to |
| official website | **P36** | url | |
| publisher (entity) | **P54** | item | prefer over the legacy P23 string |
| journal (entity) | **P57** | item | prefer over the legacy P22 string |
| page(s) | **P24** | string | |
| volume | **P25** | string | |
| issue | **P26** | string | |
| chapters | **P49** | string | chapter count or range (book excerpt) |
| duration | **P45** | quantity | seconds (song, film, video) |
| URL | **P48** | url | the work's URL |
| access URL | **P55** | url | landing page, not necessarily a file |
| file | **P56** | url | the work's `File:` page URL |
| language | **P77** | string | language the source is written in |
| developer | **P33** | item | software |
| license | **P34** | item | software or image |
| operating system | **P35** | item | software |
| user interface | **P41** | item | software |
| has use | **P39** | item | software |
| source code repository | **P37** | url | software |
| documentation URL | **P43** | url | software |
| software version | **P38** | string | software |
| replaces | **P40** | item | software |
| slogan | **P42** | monolingualtext | software |
| image | **P32** | url | `File:` page URL |
| image author | **P61** | string | free-text attribution |
| additional license information | **P62** | string | attribution, terms, credits |
| image source | **P80** | string | free-text provenance |
| parent organization | **P60** | item | collective |
| has member | **P82** | item | person in a group-of-humans collective |
| court | **P67** | item | legal case |
| territorial jurisdiction (OSM) | **P68** | external-id | `node/…`, `way/…` or `relation/…` |
| territorial jurisdiction (label) | **P69** | string | display label for P68 |
| case number | **P70** | string | |
| patent number | **P71** | external-id | |
| report number | **P72** | string | |
| legislation number | **P73** | string | |
| international | **P74** | string | marker value `yes` |
| reference code | **P78** | string | article / clause / section |

**Structural or legacy properties** — do not set these on ordinary entity creation: P9 (equivalent property), P10 (equivalent class), P11 (formatter URL), P22 (published in, string), P23 (publisher, string), P31 (subclass of), P27 (unused).
