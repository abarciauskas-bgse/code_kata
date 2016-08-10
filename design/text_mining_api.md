# Text Mining API (or Library?)

This is a design document for a hypothetical API for creating and interacting with corpora for information retrieval and other text mining objectives. (E.g. LDA)

# Resources

The text mining API has the following "primitive" resources:

* corpus
* document (belongs to corpus)
* term_dictionary (belongs to a corpus)
* document\_sub\_part (belongs to document, e.g. sentence or paragraph)
* words (belong to a document\_sub\_part)
    - has attributes: stem, pos (part-of-speech)
* stems

## Creational Design Patterns: Examples in the TMA

### `AbstractFactory`

The [`AbstractFactory`](https://sourcemaking.com/design_patterns/abstract_factory) handles handles directing instantiation to the factory for a family of related resources.

`CorporaAbstractFactory` factory could have different factory methods for creating a multi-document based corpora vs a single-document based corpora and various sub-part types (sentence, paragraph, ...).

### `Builder`

The [`Builder`](https://sourcemaking.com/design_patterns/builder) seperates the construcmtion of a complex object from its representation.

The `CorporaMultiDocumentBuilder` constructs a corpora comprised of its documents, term_dictionary, sub_parts, words, etc.

### `FactoryMethod`

The [`FactoryMethod`](https://sourcemaking.com/design_patterns/factory_method) is the interface for creating families of related objects.

The `CorporaSingleDocumentSentenceFactory` constructs a corpora using a single document and sub parts from sentences.

### `ObjectPool`

The [`ObjectPool`](https://sourcemaking.com/design_patterns/object_pool) manages creation of factory methods' instantiated objects.

The `DocumentSubPartPool` would be a pool of document sub parts (sentences).

### `Prototype`

[`Prototypes`](https://sourcemaking.com/design_patterns/prototype) enable easy creating of a new object.

`prototypes` of words exist so as to make creation of new words for a given document easy, just adding the document id would be necessary (assuming POS is always the same?).

### `Singleton`

[`Singleton`](https://sourcemaking.com/design_patterns/singleton) encapsulates the need for a class which may only have one instance.

The `language` single may be applicable in this case, if the API should only be deployed with one language. However really this can be designed for, a corpora should have a language.

...have to think on this one

----
## Structural Design Patterns

### `StemDocumentAdapter`

The `StemDocumentAdapter` adapts a stem into the context of a sub document. (Although this looks a little much like a decorator)

Their example is of a wrench with a 1/2" setting and a 1/4" socket

### `Bridge`

Decouple an abstraction from its implementation. A `DocumentSubPartBridge` takes a `DocumentSubPart` to its implementation in `Sentence` or `Paragraph` subclasses.

### `Composite`

`Paragraph` is a composite of sub parts and their words.

### `Decorator`

The `SubPartDecorator` enables the document sub part to be represented with spaces or indents, etc.

(I'm just thinking also the sub parts could be lists and tables......)

### `Facade`

ADDME


### `FlyWeight`

ADDME


### `PrivateClassData`

ADDME


### `Proxy`

ADDME

----
## Behavioral Patterns

ADDME




